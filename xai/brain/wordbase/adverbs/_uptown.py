

#calss header
class _UPTOWN():
	def __init__(self,): 
		self.name = "UPTOWN"
		self.definitions = [u'in or towards the northern part of a city or town, especially if there is not much business or industry there: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
