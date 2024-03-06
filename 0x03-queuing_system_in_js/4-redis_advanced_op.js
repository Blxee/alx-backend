import redis from 'redis';
import { promisify } from 'node:util';

const client = redis.createClient();
client.on('error', err => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

const entries = Object.entries({
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2,
});

entries.forEach(([val, hash]) => client.hset('HolbertonSchools', val, hash, redis.print));

client.hgetall('HolbertonSchools', (err, val) => console.log(val));
