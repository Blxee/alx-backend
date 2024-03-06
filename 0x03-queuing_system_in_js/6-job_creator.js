import kue from 'kue';

const queue = kue.createQueue({ name: 'push_notification_code' });

const job = queue.create('push_notification_code', {
  phoneNumber: '0585847323',
  message: 'Hello from kue!',
}).save();

job.on('enqueue', () => console.log('Notification job created:', job.id));
job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'));
