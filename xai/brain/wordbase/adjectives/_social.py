

#calss header
class _SOCIAL():
	def __init__(self,): 
		self.name = "SOCIAL"
		self.definitions = [u'relating to activities in which you meet and spend time with other people and that happen during the time when you are not working: ', u'Social people like to meet and spend time with other people: ', u'relating to society and living together in an organized way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
