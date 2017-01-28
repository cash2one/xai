

#calss header
class _CHARMED():
	def __init__(self,): 
		self.name = "CHARMED"
		self.definitions = [u"very pleased or attracted by someone's charm: ", u'to be very lucky in life, often escaping dangerous situations without being hurt']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
