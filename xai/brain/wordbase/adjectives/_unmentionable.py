

#calss header
class _UNMENTIONABLE():
	def __init__(self,): 
		self.name = "UNMENTIONABLE"
		self.definitions = [u'shocking or embarrassing, and therefore not allowed or disapproved of as a subject of conversation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
