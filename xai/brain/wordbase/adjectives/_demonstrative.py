

#calss header
class _DEMONSTRATIVE():
	def __init__(self,): 
		self.name = "DEMONSTRATIVE"
		self.definitions = [u'If you are demonstrative, you show your feelings or behave in a way that shows your love: ', u'Demonstrative words are words, for example "this", "that", "these", and "those", that show which person or thing is being referred to: ', u'to show something or make something clear: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
