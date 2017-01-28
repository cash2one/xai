

#calss header
class _PROTESTANT():
	def __init__(self,): 
		self.name = "PROTESTANT"
		self.definitions = [u'of or relating to these parts of the Christian Church: ', u'the belief that work is valuable as an activity, as well as for what it produces']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
