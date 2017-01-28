

#calss header
class _PARENTHETICAL():
	def __init__(self,): 
		self.name = "PARENTHETICAL"
		self.definitions = [u'A parenthetical remark is said in addition to the main part of what you are saying.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
