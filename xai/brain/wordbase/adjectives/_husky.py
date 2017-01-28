

#calss header
class _HUSKY():
	def __init__(self,): 
		self.name = "HUSKY"
		self.definitions = [u'A voice that is husky is low and rough, often in an attractive way, or because of illness: ', u'A husky man or boy is big and strong.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
