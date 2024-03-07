import express from 'express';
import redis from 'redis';
import { promisify } from 'node:util';

const client = redis.createClient();
client.on('error', err => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

listProducts.forEach(({ itemId, initialAvailableQuantity: stock }) => reserveStockById(itemId, stock));

function getItemById(id) {
  return listProducts.find(({ itemId }) => id === itemId);
}

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock, redis.print);
}

async function getCurrentReservedStockById(itemId) {
  const get = promisify(client.get).bind(client);
  const val = await get(`item.${itemId}`);
  return val;
}

const app = express();

app.get('/list_products', (req, res) => {
  res.send(JSON.stringify(listProducts));
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  let item = getItemById(itemId);
  if (!item) {
    res.send('{"status":"Product not found"}');
    return;
  }
  const currentQuantity = await getCurrentReservedStockById(itemId);
  item = { currentQuantity, ...item };
  res.send(JSON.stringify(item));
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    res.send('{"status":"Product not found"}');
    return;
  }
  const currentQuantity = await getCurrentReservedStockById(itemId);
  if (currentQuantity <= 0) {
    res.send(`{"status":"Not enough stock available","itemId":${itemId}}`);
    return;
  }
  reserveStockById(itemId, currentQuantity - 1);
  res.send(`{"status":"Reservation confirmed","itemId":${itemId}}`);
});

app.listen(1245);
