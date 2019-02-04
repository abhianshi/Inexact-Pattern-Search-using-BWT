import math

# Suffix Array Class
class SuffixArray:

    def createArray(self,s):
        SA = []
        m = len(s)

        # Initial Suffix Array
        # Unique Characters in History-1
        initial_characters = list(set(s))

        # Sort the unique characters for efficieny purposes
        initial_characters.sort()

        # Initialize bucket counters and bucket start indices
        bucket_counter = [0 for i in range(0, len(initial_characters))]
        bucket_start = []
        bucket_start.append(0)
        for i in range(1, len(initial_characters)):
            start_index = s.count(initial_characters[i-1]) + bucket_start[len(bucket_start)-1]
            bucket_start.append(start_index)


        # Sort the Suffix Array for History-1
        SA1 = [0 for i in range(0, m)]
        for i in range(0, m):
            bucket_id = initial_characters.index(s[i])
            SA1[bucket_start[bucket_id] + bucket_counter[bucket_id]] = i
            bucket_counter[bucket_id] += 1

        SA.append(SA1)
        H = 1

        # Count array
        C = {}
        C[initial_characters[0]] = 0
        for i in range(1,len(initial_characters)):
            C[initial_characters[i]] = C[initial_characters[i-1]] + bucket_counter[i-1]

        # Suffix Array at different Stages
        for stages in range(1, math.ceil(math.log(len(s),2))+1):
            # print("Intial Characters at Stage",stages,initial_characters)
            # print(bucket_start)
            # print(bucket_counter)
            print("Suffix Array at stage",stages)
            print()
            for i in range(0, len(SA[len(SA)-1])):
                print(i+1,"\t", SA[len(SA)-1][i],"\t", s[SA[len(SA)-1][i]:SA[len(SA)-1][i]+H])
            print()
            SA2 = [0 for i in range(0, m)]
            bucket_counter2 = [0 for i in range(0, len(initial_characters))]
            for i in range(0,m):
                j = SA[stages-1][i]

                # Singleton bucket
                end = min(j+H, len(s))
                if(bucket_counter[initial_characters.index(s[j:end])] == 1):
                    SA2[i] = j

                if((j - H) >= 0):
                    # Identify the bucket belonging to A[j-H]
                    end = min(j, len(s))
                    bucket_id = initial_characters.index(s[j-H : end])
                    p = bucket_start[bucket_id] + bucket_counter2[bucket_id]
                    SA2[p] = j - H
                    bucket_counter2[bucket_id] += 1

            SA.append(SA2)
            H = 2*H

            # initial_characters
            initial_characters = []
            # bucket_start
            bucket_start = []
            # bucket_counter
            bucket_counter = []

            initial_characters.append("$")
            bucket_start.append(0)
            start = 0
            for i in range(1,m):
                j = SA[len(SA)-1][i]
                if(s[j:j+H] != initial_characters[len(initial_characters)-1]):
                    end = min(j+H, len(s))
                    initial_characters.append(s[j:end])
                    bucket_start.append(i)
                    bucket_counter.append(i - start)
                    start = i
            bucket_counter.append(i-start+1)

        print("Count Dictionary", C)
        print()
        return SA[len(SA)-1], C


    # SA is the Suffix Array
    def Inverse(self,SA):
        m = len(SA)
        R = [0 for i in range(0, m)]
        for i in range(1, m):
            R[SA[i]] = i

        print("R Array",R)
        print()

        return R
