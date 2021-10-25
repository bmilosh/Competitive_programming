"""
--- Day 14: Reindeer Olympics ---

This year is the Reindeer Olympics! Reindeer can fly at high speeds, 
but must rest occasionally to recover their energy. Santa would like to know 
which of his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) 
or resting (not moving at all), and always spend whole seconds in either state.

For example, suppose you have the following Reindeer:

    Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.

After one second, Comet has gone 14 km, while Dancer has gone 16 km. 
After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. 
On the eleventh second, Comet begins resting (staying at 140 km), 
and Dancer continues on for a total distance of 176 km. On the 12th second, 
both reindeer are resting. They continue to rest until the 138th second, 
when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting, 
and Comet is in the lead at 1120 km (poor Dancer has only gotten 
1056 km by that point). So, in this situation, Comet would win 
(if the race ended at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), 
after exactly 2503 seconds, what distance has the winning reindeer traveled?

Your puzzle answer was 2660.

--- Part Two ---

Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.

Instead, at the end of each second, he awards one point to the 
reindeer currently in the lead. (If there are multiple reindeer 
tied for the lead, they each get one point.) He keeps the traditional 
2503 second time limit, of course, as doing otherwise would be entirely ridiculous.

Given the example reindeer from above, after the first second, 
Dancer is in the lead and gets one point. He stays in the lead 
until several seconds into Comet's second burst: after the 140th second, 
Comet pulls into the lead and gets his first point. Of course, 
since Dancer had been in the lead for the 139 seconds before that, 
he has accumulated 139 points by the 140th second.

After the 1000th second, Dancer has accumulated 689 points, 
while poor Comet, our old champion, only has 312. So, 
with the new scoring system, Dancer would win (if the race ended at 1000 seconds).

Again given the descriptions of each reindeer (in your puzzle input), 
after exactly 2503 seconds, how many points does the winning reindeer have?

Your puzzle answer was 1256.
"""


class Solution:
    def distance_traveled(self, input: str, total_time: int) -> int:
        with open(f"{input}", 'rt') as f:
            abilities = []
            for line in f.readlines():
                # line will look something like the following:
                # Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
                line = line.split()
                abilities.append([line[0], line[3], line[6], line[-2]])

        for i in range(len(abilities)):
            reindeer = abilities[i]
            reind_speed = int(reindeer[1])
            fly_time = int(reindeer[2])
            reind_time = fly_time + int(reindeer[3])
            time_rem = total_time // reind_time
            dist_run = reind_speed * fly_time * time_rem
            last_lap = total_time % reind_time

            if last_lap > fly_time:
                last_run = reind_speed * fly_time
            else:
                last_run = last_lap * reind_speed
            total_dist = last_run + dist_run

            if i == 0:
                fastest_distance = total_dist
            else:
                if fastest_distance < total_dist:
                    fastest_distance = total_dist
        
        return fastest_distance


    def distance_traveled2(self, input: str, total_time: int) -> int:

        with open(f"{input}", 'rt') as f:
            ability_dict = {}
            for line in f.readlines():
                # line will look something like the following:
                # Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
                line = line.split()

                # For each reindeer, its values are as follows:
                # 0 as a placeholder for distance travelled;
                # 0 as a placeholder for points received for being in the lead;
                # Its max consecutive run duration;
                # Its rest duration;
                # Sum of the previous two entries;
                # Its speed.
                ability_dict[line[0]] = [0, 0, int(line[6]), int(line[-2]), 
                                        int(line[-2]) + int(line[6]), 
                                        int(line[3])] 

        time_run = 0
        while time_run < total_time :
            for reindeer in ability_dict:
                if time_run % ability_dict[reindeer][4] < ability_dict[reindeer][2]:
                    # Updates the reindeer's distance travelled if not resting
                    ability_dict[reindeer][0] += ability_dict[reindeer][-1]
            current_lead = [reindeer for reindeer in ability_dict if 
                                ability_dict[reindeer][0] == max([value[0] 
                                    for value in ability_dict.values()])]
            for fast_reind in current_lead:
                # The current lead reindeers get an extra point
                ability_dict[fast_reind][1] += 1
            time_run += 1

        return max([value[1] for value in ability_dict.values()])


if __name__ == '__main__':
    # solution1 = Solution().distance_traveled('reindeer_olympics_day14.txt', 2503)
    # print(f"Fastest reindeer travelled a total distance of {solution1} km.")

    solution = Solution().distance_traveled2('reindeer_olympics_day14.txt', 2503)
    print(f"Winning reindeer receives {solution} points")