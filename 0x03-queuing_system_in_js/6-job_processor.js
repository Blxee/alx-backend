import kue from 'kue';

const queue = kue.createQueue();

queue.process('push_notification_code', (job, _done) => sendNotification(job.data.phoneNumber, job.data.message));

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}
