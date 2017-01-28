

#calss header
class _RAPIER():
	def __init__(self,): 
		self.name = "RAPIER"
		self.definitions = [u'used to describe humour or a remark that is extremely clever and funny: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
