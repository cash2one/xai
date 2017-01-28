

#calss header
class _SMILINGLY():
	def __init__(self,): 
		self.name = "SMILINGLY"
		self.definitions = [u'If you do something smilingly, you smile as you are doing it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
