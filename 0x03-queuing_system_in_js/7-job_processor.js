import kue from 'kue';

const blackList = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  if (blackList.includes(phoneNumber)) {
    job.progress(0, 100);
    throw new Error(`Phone number ${phoneNumber} is blacklisted`);
  } else {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  }
}

const queue = kue.createQueue();

queue.process('push_notification_code', function(job, done) {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
