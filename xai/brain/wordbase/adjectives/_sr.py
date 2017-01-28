

#calss header
class _SR():
	def __init__(self,): 
		self.name = "SR"
		self.definitions = [u"written abbreviation for  senior adjective , used after a man's name to refer to the older of two people in the same family who have the same name"]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
