class RepeatString:
    
    def __init__(self, data):
        assert isinstance(data, str), "Input data must be a string"
        self.data = data

    def repeat_words(self):
        words = self.data.split()
        word_count = {}

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        repeated_words = [word for word, count in word_count.items() if count > 1]
        return repeated_words

S = "python java python php python c++ javascript python"
repeat_string = RepeatString(S)
repeated_words = repeat_string.repeat_words()
print(repeated_words)
