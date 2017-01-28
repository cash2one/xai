

#calss header
class _INCESTUOUS():
	def __init__(self,): 
		self.name = "INCESTUOUS"
		self.definitions = [u'involving incest: ', u'involving only a close or limited group of people, who do not communicate or do business with people outside the group: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
