from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

# {
#   "logs": {
#     "logs_collected": {
#       "files": {
#         "collect_list": [
#           {
#             "file_path": "/home/ubuntu/video-player-website/logs/apache/apache.log",
#             "log_group_name": "apache/access",
#             "log_stream_name": "{ip_address}_{instance_id}"
#           },
#           {
#             "file_path": "/home/ubuntu/video-player-website/logs/elf/elf.log",
#             "log_group_name": "elf/access",
#             "log_stream_name": "{ip_address}_{instance_id}"
#           },
#           {
#             "file_path": "/home/ubuntu/video-player-website/logs/nginx/nginx.log",
#             "log_group_name": "nginx/access",
#             "log_stream_name": "{ip_address}_{instance_id}"
#           }
#         ]
#       }
#     }
#   }
# }

# {
#     "agent": {
#       "metrics_collection_interval": 10,
#       "logfile": "/opt/aws/amazon-cloudwatch-agent/logs/amazon-cloudwatch-agent.log",
#       "run_as_user": "root"
#     },
#     "logs": {
#       "logs_collected": {
#         "files": {
#           "collect_list": [
#             {
#               "file_path": "/opt/aws/amazon-cloudwatch-agent/logs/amazon-cloudwatch-agent.log",
#               "log_group_name": "/apps/CloudWatchAgentLog/",
#               "log_stream_name": "{ip_address}_{instance_id}",
#               "timezone": "Local"
#             },
#             {
#                 "file_path": "/home/ubuntu/video-player-website/logs/apache/apache.log",
#                 "log_group_name": "apache/access",
#                 "log_stream_name": "{ip_address}_{instance_id}"
#             },
#             {
#                 "file_path": "/home/ubuntu/video-player-website/logs/elf/elf.log",
#                 "log_group_name": "elf/access",
#                 "log_stream_name": "{ip_address}_{instance_id}"
#             },
#             {
#                 "file_path": "/home/ubuntu/video-player-website/logs/nginx/nginx.log",
#                 "log_group_name": "nginx/access",
#                 "log_stream_name": "{ip_address}_{instance_id}"
#             }
#           ]
#         }
#       }
#     }
#   }