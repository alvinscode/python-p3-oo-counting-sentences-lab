#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.value= value

  def get_value(self):
    return self._value
  
  def set_value(self, value):
    if type(value) is not str:
      print("The value must be a string.")
    self._value=value

  value=property(get_value, set_value)

  def is_sentence(self):
    return self.value.endswith('.') or self.value.endswith('?') or self.value.endswith('!')

  def is_question(self):
    return self.value.endswith("?")
  
  def is_exclamation(self):
    return self.value.endswith("!")
  
  def count_sentences(self):
    modified_value = self.value.replace('...', '.').replace('?', '.').replace('!', '.')
    sentences = modified_value.split('.')
    sentences = [sentence for sentence in sentences if sentence.strip()]
    return len(sentences)
