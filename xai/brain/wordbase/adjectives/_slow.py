

#calss header
class _SLOW():
	def __init__(self,): 
		self.name = "SLOW"
		self.definitions = [u'moving, happening, or doing something without much speed: ', u'used to describe a film, book, play, etc. that does not have much excitement and action: ', u'A person might be described as slow if they are not very clever and do not understand or notice things quickly: ', u'If a clock or watch is slow, it shows a time that is earlier than the real time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
