

#calss header
class _NEUTRAL():
	def __init__(self,): 
		self.name = "NEUTRAL"
		self.definitions = [u'not saying or doing anything that would encourage or help any of the groups involved in an argument or war: ', u'A neutral ground or field is a sports stadium that does not belong to either of the two teams taking part in a competition or game: ', u'having features or characteristics that are not easily noticed: ', u'A neutral chemical substance is neither an acid nor an alkali: ', u'A neutral object in physics has no electrical charge: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
