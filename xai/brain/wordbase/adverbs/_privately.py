

#calss header
class _PRIVATELY():
	def __init__(self,): 
		self.name = "PRIVATELY"
		self.definitions = [u'in secret, or with only one or two other people present: ', u'by a person or company and not by the government: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
