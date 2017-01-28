

#calss header
class _WARY():
	def __init__(self,): 
		self.name = "WARY"
		self.definitions = [u'not completely trusting or certain about something or someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
