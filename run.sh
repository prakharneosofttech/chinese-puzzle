echo "Running Chinese puzzle to calculate rabbits and chickens based on head_count and leg_count\n\n"
echo "Input: head_count = 10, leg_count = 22"
curl --location --request GET '127.0.0.1:8000/get_count?head_count=10&leg_count=22'
echo "\n\nInput: head_count = 10, leg_count = 20"
curl --location --request GET '127.0.0.1:8000/get_count?head_count=10&leg_count=20'
echo "\n\nInput: head_count = 9, leg_count = 19"
curl --location --request GET '127.0.0.1:8000/get_count?head_count=9&leg_count=19'
echo "\n\nInput: head_count = 8, leg_count = 18"
curl --location --request GET '127.0.0.1:8000/get_count?head_count=8&leg_count=18'
echo "\n\nInput: head_count = 7, leg_count = 17"
curl --location --request GET '127.0.0.1:8000/get_count?head_count=7&leg_count=17'
echo "\n\nInput: head_count = 6, leg_count = 16"
curl --location --request GET '127.0.0.1:8000/get_count?head_count=6&leg_count=16'
echo "\n\nInput: head_count = 5, leg_count = 15"
curl --location --request GET '127.0.0.1:8000/get_count?head_count=5&leg_count=15'
echo "\n\nInput: head_count = 5, leg_count = 14"
curl --location --request GET '127.0.0.1:8000/get_count?head_count=5&leg_count=14'
echo "\n\nInput: head_count = 5, leg_count = 13"
curl --location --request GET '127.0.0.1:8000/get_count?head_count=5&leg_count=13'