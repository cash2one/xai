

#calss header
class _AUTHORITATIVE():
	def __init__(self,): 
		self.name = "AUTHORITATIVE"
		self.definitions = [u'showing that you are confident, in control, and expect to be respected and obeyed: ', u'containing complete and accurate information, and therefore respected: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
