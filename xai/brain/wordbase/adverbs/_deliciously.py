

#calss header
class _DELICIOUSLY():
	def __init__(self,): 
		self.name = "DELICIOUSLY"
		self.definitions = [u'with a very pleasant taste or smell: ', u'very pleasantly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
