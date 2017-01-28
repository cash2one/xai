

#calss header
class _AIRSICK():
	def __init__(self,): 
		self.name = "AIRSICK"
		self.definitions = [u'having the feeling that you will vomit because of the movement of an aircraft you are travelling in']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
