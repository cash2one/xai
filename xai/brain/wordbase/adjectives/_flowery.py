

#calss header
class _FLOWERY():
	def __init__(self,): 
		self.name = "FLOWERY"
		self.definitions = [u'decorated with pictures of flowers: ', u'If a speech or writing style is flowery, it uses too many complicated words or phrases in an attempt to sound skilful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
