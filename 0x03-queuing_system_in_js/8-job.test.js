import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

queue = kue.createQueue();

before(function() {
  queue.testMode.enter();
});

afterEach(function() {
  queue.testMode.clear();
});

after(function() {
  queue.testMode.exit()
});

it('does something cool', function() {
  createPushNotificationsJobs([{}], queue);
  expect(queue.testMode.jobs.length).to.equal(2);
  expect(queue.testMode.jobs[0].type).to.equal('myJob');
  expect(queue.testMode.jobs[0].data).to.eql({ foo: 'bar' });
});
