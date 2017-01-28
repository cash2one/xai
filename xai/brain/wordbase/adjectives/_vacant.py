

#calss header
class _VACANT():
	def __init__(self,): 
		self.name = "VACANT"
		self.definitions = [u'not filled or occupied; available to be used: ', u'A vacant job is one that no one is doing and is therefore available for someone new to do: ', u'showing no interest or mental activity: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
