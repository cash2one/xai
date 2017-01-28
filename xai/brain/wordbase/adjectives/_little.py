

#calss header
class _LITTLE():
	def __init__(self,): 
		self.name = "LITTLE"
		self.definitions = [u'small in size or amount: ', u'a small amount of food or drink: ', u'a present that is not of great value: ', u'young: ', u'used to emphasize an opinion that is being given about something or someone: ', u'not very important or serious: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
