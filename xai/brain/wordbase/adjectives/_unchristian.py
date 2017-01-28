

#calss header
class _UNCHRISTIAN():
	def __init__(self,): 
		self.name = "UNCHRISTIAN"
		self.definitions = [u'not good, kind, or showing any care for other people; not showing the qualities expected of a Christian: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
