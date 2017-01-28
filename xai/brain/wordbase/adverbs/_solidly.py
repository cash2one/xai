

#calss header
class _SOLIDLY():
	def __init__(self,): 
		self.name = "SOLIDLY"
		self.definitions = [u'strongly and firmly: ', u'in a regular or continuous way, without sudden changes: ', u'agreeing with or supporting someone completely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
