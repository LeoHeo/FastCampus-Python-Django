user_list = [
    ["허진한", "주소1"],
    ["안수찬", "주소2"],
]

# List의 List => Dict의 List로 변경하기
      
# 원시적인 방법
user_list_change = []
for value in user_list:
    user_list_change.append(
        {
            "name": value[0],
            "addredd": value[1]
        }
    )

# List Comprehension
# for문 앞은 lambda같은 존재
def get_user_dict(user):
    return {
        "name": user[0],
        "address": user[1]
    }

[
    # get_user_dict(user)
    {
        "name": user[0],
        "address": user[1]
    },
    for user
    in user_list
]
