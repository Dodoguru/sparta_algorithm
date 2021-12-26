import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


def get_min_city_chicken_distance(n, m, city_map):
    chicken_location_list = []
    home_location_list = []
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1: # city_map[i][j]의 값이 1이라면 가정집이라는 것이다.
                home_location_list.append([i, j])
                print("가정집 리스트 : ", home_location_list)
            if city_map[i][j] == 2: # city_map[i][j]의 값이 2라면 치킨집이라는 것이다.
                chicken_location_list.append([i, j])
                print("치킨집 리스트 : ", chicken_location_list)

# 치킨집 중에 M개 고르기
    chicken_location_m_combinations = list(itertools.combinations(chicken_location_list, m))
    min_distance_of_m_combinations = sys.maxsize
    print("min_distance_of_m_combinations : ", min_distance_of_m_combinations)
    for chicken_location_m_combinations in chicken_location_m_combinations:
        distance = 0
        for home_r, home_c in home_location_list : # home_r과 home_c는 home_location_list 배열에 있는 것이다.
            print("home_r :", home_r)
            print("home_c :", home_c)
            min_home_chicken_distance = sys.maxsize
            print("min_home_chicken_distance : ", str(min_home_chicken_distance))
            for chicken_location in chicken_location_m_combinations:
                print("chicken_location : ", str(chicken_location))
                min_home_chicken_distance = min(
                    min_home_chicken_distance,
                    abs(home_r - chicken_location[0]) + abs(home_c - chicken_location[1])
                )
            print("min_home_chicken_distance : ", min_home_chicken_distance)
            distance += min_home_chicken_distance
        min_distance_of_m_combinations = min(min_distance_of_m_combinations, distance)
    return min_distance_of_m_combinations

# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!
print("hihihi")