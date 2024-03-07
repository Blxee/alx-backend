import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'node:util';

const client = redis.createClient();
client.on('error', err => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

const queue = kue.createQueue({ name: 'push_notification_code' });

const app = express();

function reserveSeat(number) {
  client.set('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const get = promisify(client.get).bind(client);
  const val = parseInt(await get('available_seats'));
  return val;
}

const reservationEnabled = true;

app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: '' + availableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: "Reservation are blocked" });
    return;
  }
  const job = queue.create('reserve_seat').save();
  job.on('enqueue', () => res.json('{ "status": "Reservation in process" }'))
    .on('complete', () => console.log(`Seat reservation job ${job.id} completed`))
    .on('failed', (err) => {
      res.json({ status: "Reservation failed" });
      console.log(`Seat reservation job ${job.id} failed:`, err)
    });
});

app.get('/process', async (req, res) => {
  queue.process('reserve_seat', async function(job, done) {
    let availableSeats = await getCurrentAvailableSeats();
    availableSeats -= 1;
    if (availableSeats <= 0) {
      reservationEnabled = false;
    }
    if (availableSeats < 0) {
      throw new Error('Not enough seats available');
    }
    reserveSeat(availableSeats);
  });
  res.json({ status: "Queue processing" });
});

client.set('available_seats', 50);
app.listen(1245);
