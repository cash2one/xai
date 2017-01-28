

#calss header
class _FORCIBLE():
	def __init__(self,): 
		self.name = "FORCIBLE"
		self.definitions = [u'Forcible actions involve the use of physical power or of violence: ', u"happening or done against someone's wishes, especially with the use of physical force: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
