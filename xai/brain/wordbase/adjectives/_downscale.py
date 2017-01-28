

#calss header
class _DOWNSCALE():
	def __init__(self,): 
		self.name = "DOWNSCALE"
		self.definitions = [u'low in quality and cheap in price; relating to or intended for people who are poor or not educated: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
