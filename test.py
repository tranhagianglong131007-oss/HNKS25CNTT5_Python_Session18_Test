players = [
    {
        "id": "CT007",
        "name": "Nguyen Quang Hai",
        "matches": 10,
        "goals": 5,
        "assists": 4,
    }
]

# hàm tính điểm hiệu suất
def performence_score(matches, goals, assitsts):
    score = (matches * 1 ) + (goals * 3) + (assitsts * 2)
    return score

def rank_performence(score):
    if score < 15:
        return "Cần thanh lý/Cho mượn"
    elif 15 <= score < 30:
        return "Dự bị chiến lược"
    elif 30 <= score < 50:
        return "Trụ cột đội bóng"
    else:
        return "Ngôi sao đẳng cấp"
    
def print_player(list_player):
    if len(list_player) == 0:
        print("Danh sách cầu thủ đang trống")
    else:
        print("Mã cầu thủ |  Tên cầu thủ |  Số trận thi đấu |  Số bàn thắng được ghi | Số đường kiến tạo | Điểm hiệu suất | Phân loại phong độ    ")
        for index , player in enumerate(list_player):
            score = performence_score(player['matches'], player['goals'], player['assists'] )
            rank = rank_performence(score)
            print(f"{index + 1}| {player['id']} | {player['name']} |  {player['matches']}| {player['goals']} | {player['assists']} |  {score}|  {rank}")

def check_id():
    while True:
        id_player = input("Nhập mã cầu thủ mới: ").strip().upper()
        if id_player == "":
            print("Mã cầu thủ không được để trống !")
            continue
        flag = False
        for player in players:
            if player["id"] == id_player:
                flag = True
                break
        if flag:
            print("mã cầu thủ đã tồn tại")
            continue
        return id_player

def add_player(players):
    id_player = check_id()

    while True:
        name = input("Nhập tên cầu thủ mới: ").strip()

        if name == "":
            print("Tên cầu thủ không được để trống!")
            continue

        break

    while True:
        try:
            matches = int(input("Nhập số trận thi đấu: "))

            if matches < 0 or matches > 50:
                print("Số trận thi đấu phải từ 0 đến 50!")
                continue

            break

        except :
            print("Vui lòng nhập số nguyên!")

    while True:
        try:
            goals = int(input("Nhập số bàn thắng: "))

            if goals < 0:
                print("Số bàn thắng phải >= 0")
                continue

            break

        except:
            print("Vui lòng nhập số nguyên!")

    while True:
        try:
            assists = int(input("Nhập số kiến tạo: "))

            if assists < 0:
                print("Số kiến tạo phải >= 0")
                continue

            break

        except:
            print("Vui lòng nhập số nguyên!")

    score =performence_score(matches,goals,assists )
    rank = rank_performence(score)

    players.append({
        "id": id_player,
        "name": name,
        "matches": matches,
        "goals": goals,
        "assists": assists,
        "performance": score,
        "rank": rank
    })

    print("Thêm cầu thủ thành công!")

def update_player(player):
    while True:
        update_id = input("Nhập mã cầu thủ muốn cập nhật: ").strip().upper()
        if update_id == "":
            print("Mã cầu thủ không được để trống ")
            continue
        
        for pls in players:
            if pls["id"] == update_id:
                while True:
                    try:
                        new_matches = int(input("Nhập số trận thi đấu: "))

                        if new_matches < 0 or new_matches > 50:
                            print("Số trận thi đấu phải từ 0 đến 50!")
                            continue

                        break

                    except :
                        print("Vui lòng nhập số nguyên!")

                while True:
                    try:
                        new_goals = int(input("Nhập số bàn thắng: "))

                        if new_goals < 0:
                            print("Số bàn thắng phải >= 0")
                            continue

                        break

                    except:
                        print("Vui lòng nhập số nguyên!")

                while True:
                    try:
                        new_assists = int(input("Nhập số kiến tạo: "))

                        if new_assists < 0:
                            print("Số kiến tạo phải >= 0")
                            continue

                        break

                    except:
                        print("Vui lòng nhập số nguyên!") 
                        
                score =performence_score(new_matches,new_goals,new_assists )
                rank = rank_performence(score)
                
                pls["matches"] = new_matches
                pls["goals"] = new_goals
                pls["assists"] = new_assists
                pls["performance"] = score
                pls["rank"] = rank

                print("Cập nhật thành công!")
                return
        print("Không tìm thấy cầu thủ")

def delete_player(players):
    while True:
        delete_id = input("Nhập mã cầu thủ muốn xóa: ").strip().upper()

        if delete_id == "":
            print("Mã cầu thủ không được để trống")
            continue

        for player in players:
            if player['id'] == delete_id:
                print(f"Tìm thấy cầu thủ: {player['name']}")

                while True:
                    confirm = input("Bạn có chắc muốn xóa? (Y/N): ").strip().upper()

                    if confirm == "Y":
                        players.remove(player)
                        print("Xóa cầu thủ thành công!")
                        return

                    elif confirm == "N":
                        print("Đã hủy thao tác xóa.")
                        return

                    else:
                        print("Vui lòng nhập Y hoặc N!")

        print("Không tìm thấy cầu thủ")

def find_player(players):
    while True:
        choose = input("""
                1. Tim kiem chinh xac theo ID
                2. tim kiem gan dung theo ten CT
                3. thoat chuong trinh
                """)
        match choose:
            case "1":
                while True:
                    lst= []
                    find_id = input("Nhap ma CT muon tim kiem ")
                    if find_id == "":
                        print("Ma cau thu khong duoc de trong")
                        continue
                    for i in players:
                        if i['id'] == find_id:
                            lst.append(i)
                    if len(lst) != 0:
                        for index, value in enumerate(lst, start=1):
                            print(f"STT: {index} | id: {value['id']} | Họ và tên: {value['name']}")
                    break
            
            case "2":
                while True:
                    lst =[]
                    find_name = input("Nhap ten cau thu muon tim kiem")
                    if find_name == "":
                        print("Ten khong dc de trong ")
                    for i in players:
                        if find_name in i["name"]:
                            lst.append(i)
                    if len(lst) != 0:
                        for index, value in enumerate(lst, start=1):
                            print(f"STT: {index} | id: {value['id']} | Họ và tên: {value['name']}")
                    break



def thong_ke_phong_do(players):
    if len(players) == 0:
        print("Danh sách cầu thủ hiện đang trống!")
        return
    ngoi_sao = 0
    tru_cot = 0
    du_bi = 0
    can_thanh_ly = 0
    for player in players:
        score = performence_score(player['matches'],player['goals'],player['assists'] )
        rank = rank_performence(score)
        if rank == "Cần thanh lý / Cho mượn":
            can_thanh_ly += 1
        elif rank == "Dự bị chiến lược":
            du_bi += 1
        elif rank == "Trụ cột đội bóng":
            tru_cot += 1
        else :
            ngoi_sao += 1
            
        print(f"Ngôi sao đẳng cấp: {ngoi_sao}")
        print(f"Trụ cột đội bóng: {tru_cot}")
        print(f"Dự bị chiến lược: {du_bi}")
        print(f"Cần thanh lý/Cho mượn: {can_thanh_ly}")
def main():
    while True:
        print("""
        =============== Menu =================
        1. Hiển thị danh sách cầu thủ
        2. Tiếp nhận cầu thủ mới
        3. Cập thật thông tin và chỉ số
        4. Xóa cầu thủ ( thanh lí hợp đồng)
        5. Tìm kiếm cầu thủ
        6. Thống kê phân loại phong độ
        7. Thoát chương trình
""")
        choice = int(input("Chọn chức năng (1 - 7): "))
        match choice:
            case 1:
                print_player(players)
            case 2:
                add_player(players)
            case 3:
                update_player(players)
            case 4:
                delete_player(players)
            case 6:
                thong_ke_phong_do(players)
            case 7:
                print("Thoát chương trình")
                break
            case _:
                print("Lựa chọn không hợp lệ!")

main()