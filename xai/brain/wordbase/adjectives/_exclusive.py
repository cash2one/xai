

#calss header
class _EXCLUSIVE():
	def __init__(self,): 
		self.name = "EXCLUSIVE"
		self.definitions = [u'limited to only one person or group of people: ', u'expensive and only for people who are rich or of a high social class: ', u'not including something: ', u'not possible at the same time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
