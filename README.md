# covid19-india_statewise_update
Update notification for Coronavirus state wise and India wise directly to your slack
Install slack on your phone and get notified 

You need Python
You need a Slack account + Slack Webhook to send slack notifications to your account
Install dependencies by running

pip install tabulate
pip install requests
pip install beautifulsoup4

Clone this repo
Write your Slack Webhook

DEFAULT_SLACK_WEBHOOK = 'https://hooks.slack.com/services/<your custome webhook url>'


Setup the cron job to receive updates whenever something changes

crontab -e 
# now write the following to run the bot every 5 mins
*/5 * * * * cd $PATH_TO_CLONE_DIR; python3 corona_bot.py --states 'haryana,maharashtra'
# to receive updates for all states, ignore the --states flag
