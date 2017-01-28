

#calss header
class _MOULDY():
	def __init__(self,): 
		self.name = "MOULDY"
		self.definitions = [u'covered with mould: ', u'of little value; unpleasant: ', u'not modern or interesting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
