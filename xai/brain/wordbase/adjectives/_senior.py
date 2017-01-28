

#calss header
class _SENIOR():
	def __init__(self,): 
		self.name = "SENIOR"
		self.definitions = [u'high or higher in rank: ', u'older and more experienced than the other members of a team: ', u'older: ', u"used after a man's name to refer to the older of two people in the same family who have the same name: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
