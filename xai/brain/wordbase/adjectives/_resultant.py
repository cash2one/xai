

#calss header
class _RESULTANT():
	def __init__(self,): 
		self.name = "RESULTANT"
		self.definitions = [u'caused by the event or situation that you have just mentioned']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
