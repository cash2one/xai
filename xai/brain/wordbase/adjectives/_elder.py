

#calss header
class _ELDER():
	def __init__(self,): 
		self.name = "ELDER"
		self.definitions = [u'a sister/brother/son/daughter who is older than the other sister(s), brother(s), etc.', u'the older person of two people: ', u"used after someone's name to show that they are the older of two people who have the same name, especially a father and son: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
