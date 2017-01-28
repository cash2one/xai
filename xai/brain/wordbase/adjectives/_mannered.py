

#calss header
class _MANNERED():
	def __init__(self,): 
		self.name = "MANNERED"
		self.definitions = [u'A mannered style of speech or behaviour is artificial, or intended to achieve a particular effect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
