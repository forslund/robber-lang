from mycroft.skills import MycroftSkill
from mycroft.skills.mycroft_skill.decorators import skill_api_method

class RobberSkill(MycroftSkill):
    @skill_api_method
    def robber_lang(self, sentence):
        """Encode a sentence to "Rövarspråket".

        Each consonant gets converted to consonant + "o" + consonant,
        vowels are left as is.

        Returns: (str) sentence in the robber language.
        """
        wovels = "aeiouyåäö"
        tokens = []
        for char in sentence.lower():
            if char not in wovels and char.isalpha():
                tokens.append(char + 'o' + char)
            else:
                tokens.append(char)
        return ' '.join(tokens)


def create_skill():
    return RobberSkill()
