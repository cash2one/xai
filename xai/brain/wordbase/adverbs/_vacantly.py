

#calss header
class _VACANTLY():
	def __init__(self,): 
		self.name = "VACANTLY"
		self.definitions = [u'showing no interest or mental activity: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
