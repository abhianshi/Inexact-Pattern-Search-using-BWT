class MergeIntervals:
    def merge(self,I):
        I = sorted(I, key=lambda start: start[0])
        merged = []
        for higher in I:
            if not merged:
                merged.append(higher)
            else:
                lower = merged[-1]
                if higher[0] <= (lower[1]+1):
                    upper_bound = max(lower[1], higher[1])
                    merged[-1] = (lower[0], upper_bound)
                else:
                    merged.append(higher)
        return merged
