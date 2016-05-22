from parkman.gateways.twitter import TwitterGateway
from parkman.utils.collection import CollectionUtil
import csv

class FileWriter:

    @classmethod
    def write_original_tweets_to_file(cls, screen_name, number_of_tweets, file_path):
        f = open(file_path, 'w')
        for tweet in TwitterGateway().get_original_tweets(screen_name, number_of_tweets):
            try:
                f.write(str(tweet) + "\n")
            except Exception as e:
                continue

    @classmethod
    def print_tweets(cls, screen_name, number_of_tweets):
        main_file = open('main.csv', 'w')
        status_file = open('status.csv', 'w')
        mainFieldNames = ['screen_name', 'status_id', 'in_reply_to_status_id']
        statusFieldNames = ['status_id', 'status_text', 'timestamp']
        main_writer = csv.DictWriter(main_file, fieldnames=mainFieldNames)
        status_writer = csv.DictWriter(status_file, fieldnames=statusFieldNames)
        for tweet in TwitterGateway().get_all_tweets_for_user(screen_name, number_of_tweets):
            try:
                print tweet.id_str
                print tweet.in_reply_to_status_id_str
                print tweet.text
                main_writer.writerow({'screen_name': screen_name, 'status_id': tweet.id_str, 'in_reply_to_status_id': tweet.in_reply_to_status_id_str})
                status_writer.writerow({'status_id': tweet.id_str, 'status_text': tweet.text.encode('utf-8'), 'timestamp': tweet.created_at})
            except Exception as e:
                print e
                continue

    @classmethod
    def get_bulk_statuses(cls, file_path, output_path):
        f = open(file_path, 'r')
        status_ids = f.read().splitlines()
        status_ids = [int(status_id) for status_id in status_ids if status_id]
        mainFieldNames = ['screen_name', 'status_id', 'in_reply_to_status_id']
        statusFieldNames = ['status_id', 'status_text', 'timestamp']
        
        main_file = open('main.csv', 'w')
        status_file = open(output_path, 'w')
        
        main_writer = csv.DictWriter(main_file, fieldnames=mainFieldNames)
        status_writer = csv.DictWriter(status_file, fieldnames=statusFieldNames)
        for tweet in TwitterGateway().get_bulk_statuses(status_ids):
            try:
                main_writer.writerow({'screen_name': tweet.user.screen_name, 'status_id': tweet.id_str, 'in_reply_to_status_id': tweet.in_reply_to_status_id_str})
                status_writer.writerow({'status_id': tweet.id_str, 'status_text': tweet.text.encode('utf-8'), 'timestamp': tweet.created_at})
            except Exception as e:
                print e
                continue
