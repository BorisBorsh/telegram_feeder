from commands import run_command

def parse_response_and_run_command(response):
    """Parse response and run command."""
    for update in response.json()['result']:
        chat_id = update['message']['chat']['id']
        command = update['message']['text']

        commands.run_command(chat_id, command)

        # if command == '/schl':
        #     schedule_message = show_schedule.get_schedule_and_portions_message(portions_on_schedule_dict)
        #     send_message.send_text(chat_id, schedule_message)
        # else:
        #     commands.run_command(chat_id, command)