from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, cap: int):
        self.cap = cap
        self.min_freq = 0
        self.key_val = {}          # key -> value
        self.key_freq = {}         # key -> freq
        self.freq_map = defaultdict(OrderedDict)  # freq -> {key: None}

    def _update_freq(self, key: int):
        freq = self.key_freq[key]
        del self.freq_map[freq][key]
        if not self.freq_map[freq]:
            del self.freq_map[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        self.key_freq[key] = freq + 1
        self.freq_map[freq + 1][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_val:
            return -1
        self._update_freq(key)
        return self.key_val[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.key_val:
            self.key_val[key] = value
            self._update_freq(key)
            return
        if len(self.key_val) == self.cap:
            # remove LFU key
            lfu_key, _ = self.freq_map[self.min_freq].popitem(last=False)
            del self.key_val[lfu_key]
            del self.key_freq[lfu_key]
            if not self.freq_map[self.min_freq]:
                del self.freq_map[self.min_freq]
        self.key_val[key] = value
        self.key_freq[key] = 1
        self.freq_map[1][key] = None
        self.min_freq = 1
